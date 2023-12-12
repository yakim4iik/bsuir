import React, { useEffect, useState } from "react";
import { Button, Col, Container, Row } from "react-bootstrap";
import { getOrganizations, removeOrganization } from "../http/organizationAPI";
import { useNavigate } from "react-router-dom";
import { ORGANIZATION_PATH } from "../utils/paths";
import { ReactComponent as Cross } from '../img/cross.svg';

export default function OrganizationList() {
    const [organizations, setOrganizations] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    useEffect(() => {
        getOrganizations().then((complaints) => {
            setOrganizations(complaints);
            setIsLoaded(true);
        })
    }, []);
    const navigate = useNavigate();
    if (!isLoaded) {
        return <div />
    }

    const onDeleteOrganization = (organization, index) => {
        removeOrganization(organization)
        const updatedOrganizations = [...organizations]
        updatedOrganizations.splice(index, 1)
        setOrganizations(updatedOrganizations);
    }

    return (
        <Container className='col-md'>
            <h3 className='mt-4'>Organizations</h3>
            {
                organizations.map((organization, index) => {
                    return <div key={organization.id} className='w-100 p-3 d-flex'
                        style={{ background: index % 2 ? '#edf4f6' : 'white' }}>
                        <Container className='ms-3 clickable' onClick={() => navigate(ORGANIZATION_PATH + organization.id)}>
                            <Row>
                                <Col md='auto'>
                                    <b>
                                        {organization.code}
                                    </b>
                                </Col>
                                <Col>
                                    {organization.name}
                                </Col>
                                <Col>
                                    {organization.phone}
                                </Col>

                                <Col>
                                    {organization.email}
                                </Col>

                                <Col>
                                    {organization.address}
                                </Col>
                                <Col>
                                    <button onClick={(e) => {
                                        e.stopPropagation();
                                        onDeleteOrganization(organization, index)
                                    }}><Cross /></button>
                                </Col>

                            </Row>
                        </Container>


                    </div>
                })
            }
            <Button className="mt-4" type="submit" onClick={() => navigate(ORGANIZATION_PATH)}>Add</Button>
        </Container>
    )
}
