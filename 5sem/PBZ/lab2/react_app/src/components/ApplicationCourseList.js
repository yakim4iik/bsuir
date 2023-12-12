import React, { useEffect, useState } from "react";
import { Button, Col, Container, Row } from "react-bootstrap";
import { getApplicationCourses, removeApplicationCourse } from "../http/applicationCourseAPI";
import { getFio } from "../utils/formMessage";
import { ReactComponent as Cross } from '../img/cross.svg';
import NewApplicationCourseModal from "./NewApplicationCourseModal";


export default function ApplicationCourseList({ applicationId }) {
    const [applicationCourses, setApplicationCourses] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [isAdd, setIsAdd] = useState(false);
    useEffect(() => {
        getApplicationCourses(applicationId).then((complaints) => {
            setApplicationCourses(complaints);
            setIsLoaded(true);
        })
    }, [applicationId]);
    if (!isLoaded) {
        return <div />
    }

    const onDeleteApplicationCourse = (applicationCourse, index) => {
        removeApplicationCourse(applicationCourse)
        const updated = [...applicationCourses]
        updated.splice(index, 1)
        setApplicationCourses(updated);
    }
    return (
        <Container className='col-md'>
            <h3 className='mt-4'>ApplicationCourses</h3>
            <div className='w-100 p-3 d-flex'>
                <Container className='ms-3 '>
                    <Row>
                        <Col >
                            <b>
                                Employee
                            </b>
                        </Col>
                        <Col>
                            <b>
                                Course
                            </b>
                        </Col>
                        <Col>
                            <b>
                                Date
                            </b>
                        </Col>
                        <Col>
                        </Col>
                    </Row>
                </Container>

            </div>
            {
                applicationCourses.map((applicationCourse, index) => {
                    return <div key={applicationCourse.id} className='w-100 p-3 d-flex'
                        style={{ background: index % 2 ? '#edf4f6' : 'white' }}>
                        <Container className='ms-3' >
                            <Row>
                                <Col>
                                    {applicationCourse.applicationCourseId?.employee ? getFio(applicationCourse.applicationCourseId?.employee) : ''}
                                </Col>

                                <Col>
                                    {(applicationCourse.applicationCourseId?.course?.code ?? '') + ' ' + (applicationCourse.applicationCourseId?.course?.name ?? '')}
                                </Col>

                                <Col>
                                    {new Date(applicationCourse.date).toLocaleDateString()}
                                </Col>
                                <Col>
                                    <button onClick={() => {
                                        onDeleteApplicationCourse(applicationCourse, index)
                                    }}>
                                        <Cross />
                                    </button>
                                </Col>

                            </Row>
                        </Container>
                    </div>
                })
            }
            <Button className="mt-4" type="submit" onClick={() => setIsAdd(true)}>Add</Button>
            <NewApplicationCourseModal
                applicationCourses={applicationCourses}
                applicationId={applicationId}
                onHide={() => setIsAdd(false)}
                setApplicationCourses={setApplicationCourses}
                show={isAdd}
            />
        </Container>
    )
}
