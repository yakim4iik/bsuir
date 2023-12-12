import React, { useEffect, useState } from "react";
import { Button, Col, Container, Row } from "react-bootstrap";
import { getApplications, removeApplication } from "../http/applicationAPI";
import { useNavigate } from "react-router-dom";
import { APPLICATION_PATH } from "../utils/paths";
import { ReactComponent as Cross } from '../img/cross.svg';

export default function ApplicationList({ organizationId }) {
    const [applications, setApplications] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    useEffect(() => {
        getApplications(organizationId).then((complaints) => {
            setApplications(complaints);
            setIsLoaded(true);
        })
    }, []);
    const navigate = useNavigate();
    if (!isLoaded) {
        return <div />
    }

    return (
        <Container className='col-md'>
            <h3 className='mt-4'>Applications</h3>
            <div className='w-100 p-3 d-flex'>
                <Container className='ms-3 '>
                    <Row>
                        <Col >
                            <b>
                                Name
                            </b>
                        </Col>
                        <Col>
                            <b>
                                Phone
                            </b>
                        </Col>
                        <Col>
                            <b>
                                Email
                            </b>
                        </Col>

                        <Col>
                            <b>
                                Address
                            </b>
                        </Col>

                        <Col>
                            <b>
                                Employees
                            </b>
                        </Col>

                    </Row>
                </Container>


            </div>
            {
                applications.map((application, index) => {
                    return <div key={application.id} className='w-100 p-3 d-flex'
                        style={{ background: index % 2 ? '#edf4f6' : 'white' }}>
                        <Container className='ms-3 clickable' onClick={() => navigate(APPLICATION_PATH + application.id)}>
                            <Row>
                                <Col>
                                    {application.name}
                                </Col>
                                <Col>
                                    {application.phone}
                                </Col>

                                <Col>
                                    {application.email}
                                </Col>

                                <Col>
                                    {application.address}
                                </Col>
                                <Col>
                                    {application.employees}
                                </Col>

                            </Row>
                        </Container>


                    </div>
                })
            }
            <Button className="mt-4" type="submit" onClick={() => navigate(APPLICATION_PATH, { state: { organizationId } })}>Add</Button>
        </Container>
    )
}
