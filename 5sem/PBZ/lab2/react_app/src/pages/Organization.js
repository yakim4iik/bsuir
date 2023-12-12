import React, { useEffect, useState } from "react";
import { Button, Container, Form } from "react-bootstrap";
import { addOrganization, getOrganizations, updateOrganization } from "../http/organizationAPI";
import { useNavigate, useParams } from "react-router-dom";
import { ORGANIZATION_PATH } from "../utils/paths";
import CourseList from "../components/CourseList";
import ApplicationList from "../components/ApplicationList";

export default function Organization() {
    const params = useParams();
    const navigate = useNavigate();

    const organizationId = +params.id;
    const isCreateOrganization = params.id === undefined;
    const [organization, setOrganization] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);

    const [code, setCode] = useState('');
    const [name, setName] = useState('');
    const [phone, setPhone] = useState('');
    const [email, setEmail] = useState('');
    const [address, setAddress] = useState('');

    useEffect(() => {
        if (isCreateOrganization) {
            setIsLoaded(true);
            return;
        }
        getOrganizations().then((organizations) => {
            const result = organizations.find((organization) => organizationId === organization.id)
            if (result) {
                setOrganization(result);
                setPhone(result.phone);
                setEmail(result.email);
                setAddress(result.address);
            }
            setIsLoaded(true);
        });


       
    }, [organizationId, isCreateOrganization]);

    const onSubmit = (event) => {
        event.preventDefault();
        const body = { ...organization, phone, email, address }
        if (isCreateOrganization) {
            body.code = code
            body.name = name
            addOrganization(body).then(id => {
                setIsLoaded(false);
                navigate(ORGANIZATION_PATH + id)
            })
        } else {
            updateOrganization(body)
        }
    }

    if (!isLoaded) {
        return <div />
    }
    if (!organization && !isCreateOrganization) {
        return <p className='error-not-found'>Not found</p>;
    }

    return (
        <Container className='col-md'>
            {
                isCreateOrganization ?
                    <h3 className='mt-3'>New organization</h3> :
                    <h3 className='mt-3'>Organization {organization.code || '№' + organization.id}, {organization.name}</h3>
            }

            <Form onSubmit={onSubmit}>
                {
                    isCreateOrganization && <>
                        <Form.Group className="mb-3" >
                            <Form.Label>Code</Form.Label>
                            <Form.Control type="text" placeholder="code" value={code} onChange={e => setCode(e.target.value)} />
                        </Form.Group>
                        <Form.Group className="mb-3" >
                            <Form.Label>Name</Form.Label>
                            <Form.Control type="text" placeholder="name" value={name} onChange={e => setName(e.target.value)} />
                        </Form.Group>
                    </>
                }

                <Form.Group className="mb-3" >
                    <Form.Label>Phone</Form.Label>
                    <Form.Control type="text" placeholder="phone" value={phone} onChange={e => setPhone(e.target.value)} />
                </Form.Group>
                <Form.Group className="mb-3" >
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="name@example.com" value={email} onChange={e => setEmail(e.target.value)} />
                </Form.Group>
                <Form.Group className="mb-3" >
                    <Form.Label> Address</Form.Label>
                    <Form.Control type="text" placeholder="address" value={address} onChange={e => setAddress(e.target.value)} />
                </Form.Group>
                <Button type="submit">{isCreateOrganization ? 'Create' : 'Update'}</Button>
            </Form>



            {
                !isCreateOrganization &&
                <>
                    <CourseList organizationId={organizationId} />
                    <ApplicationList organizationId={organizationId} />
                </>
            }
        </Container>
    )
}
