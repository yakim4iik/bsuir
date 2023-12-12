import React, { useEffect, useState } from "react";
import { Button, Col, Container, Form, Row } from "react-bootstrap";
import { getCourses, removeCourse } from "../http/courseAPI";
import { useNavigate } from "react-router-dom";
import { COURSE_PATH, ORGANIZATION_PATH } from "../utils/paths";
import { ReactComponent as Cross } from '../img/cross.svg';

export default function CourseList({ organizationId }) {
    const [courses, setCourses] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [date, setDate] = useState('');
    useEffect(() => {
        getCourses(organizationId, date).then((complaints) => {
            setCourses(complaints);
            setIsLoaded(true);
        })
    }, [date, organizationId]);
    const navigate = useNavigate();
    if (!isLoaded) {
        return <div />
    }

    const onDeleteCourse = (course, index) => {
        removeCourse(course)
        const updatedCourses = [...courses]
        updatedCourses.splice(index, 1)
        setCourses(updatedCourses);
    }

    return (
        <Container className='col-md'>
            <h3 className='mt-4'>Courses</h3>
            <Form>
                <Form.Group className="mb-3" >
                    <Form.Label>Date</Form.Label>
                    <Form.Control type="date" value={date} onChange={e => setDate(e.target.value)} />
                </Form.Group>
            </Form>
            <div className='w-100 p-3 d-flex'>
                <Container className='ms-3 '>
                    <Row>
                        <Col md='auto'>
                            <b>
                                Code
                            </b>
                        </Col>
                        <Col>
                            <b>
                                Name
                            </b>
                        </Col>
                        <Col>
                            <b>
                                Type
                            </b>
                        </Col>

                        <Col>
                            <b>
                                Number of days
                            </b>
                        </Col>

                        <Col>
                            <b>
                                Number of students
                            </b>
                        </Col>
                        <Col>
                            <b>
                                {'Price (NDS)'}
                            </b>
                        </Col>
                        <Col>
                        </Col>


                    </Row>
                </Container>


            </div>
            {
                courses.map((course, index) => {
                    return <div key={course.id} className='w-100 p-3 d-flex'
                        style={{ background: index % 2 ? '#edf4f6' : 'white' }}>
                        <Container className='ms-3 clickable' onClick={() => navigate(COURSE_PATH + course.id)}>
                            <Row>
                                <Col md='auto'>
                                    <b>
                                        {course.code}
                                    </b>
                                </Col>
                                <Col>
                                    {course.name}
                                </Col>
                                <Col>
                                    {course.type?.name ?? "-"}
                                </Col>

                                <Col>
                                    {course.days}
                                </Col>

                                <Col>
                                    {course.students}
                                </Col>

                                <Col>
                                    {course.price != null ? course.price + ' (' + course.priceNds + ')' : '-'}
                                </Col>

                                <Col>
                                    <button onClick={(e) => {
                                        e.stopPropagation();
                                        onDeleteCourse(course, index)
                                    }}><Cross /></button>
                                </Col>

                            </Row>
                        </Container>


                    </div>
                })
            }
            <Button className="mt-4" type="submit" onClick={() => navigate(COURSE_PATH, { state: { organizationId } })}>Add</Button>
        </Container>
    )
}
