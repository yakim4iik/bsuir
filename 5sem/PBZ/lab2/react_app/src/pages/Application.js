import React, { useEffect, useState } from "react";
import { Button, Container, Form } from "react-bootstrap";
import { addApplication, getApplications, updateApplication } from "../http/applicationAPI";
import { useNavigate, useParams, useLocation } from "react-router-dom";
import { APPLICATION_PATH } from "../utils/paths";
import ApplicationCourseList from "../components/ApplicationCourseList";


export default function Application() {
    const params = useParams();
    const navigate = useNavigate();
    const location = useLocation();

    const applicationId = +params.id;
    const isCreateApplication = params.id === undefined;
    const [application, setApplication] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [isEdit, setIsEdit] = useState(false);

    const [name, setName] = useState('');
    const [phone, setPhone] = useState('');
    const [email, setEmail] = useState('');
    const [address, setAddress] = useState('');


    useEffect(() => {
        if (isCreateApplication) {
            setIsLoaded(true);
            return;
        }
        getApplications().then((applications) => {
            const result = applications.find((application) => applicationId === application.id)
            if (result) {
                setApplication(result);
                setPhone(result.phone);
                setEmail(result.email);
                setAddress(result.address);
            }
            setIsLoaded(true);
        });
    }, [applicationId, isCreateApplication]);

    const onSubmit = (event) => {
        event.preventDefault();
        const body = { ...application, phone, email, address}
        if (isCreateApplication) {
            body.name = name
            body.organization = { id: location.state.organizationId }
            addApplication(body).then(id => {
                setIsLoaded(false);
                navigate(APPLICATION_PATH + id)
            })
        } else {
            updateApplication(body)
        }
    }

    if (!isLoaded) {
        return <div />
    }
    if (!application && !isCreateApplication) {
        return <p className='error-not-found'>Not found</p>;
    }

    return (
        <Container className='col-md'>
            {
                isCreateApplication ?
                    <h3 className='mt-3'>New application</h3> :
                    <h3 className='mt-3'>Application {'№' + application.id}, {application.name}</h3>
            }
            <Form onSubmit={onSubmit}>
                {
                    isCreateApplication && <>
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

                <Button type="submit">{isCreateApplication ? 'Create' : 'Update'}</Button>
            </Form>

            {
                !isCreateApplication &&
                <>
                    <ApplicationCourseList applicationId={applicationId}/>
                </>
            }

        </Container>
    )
}
