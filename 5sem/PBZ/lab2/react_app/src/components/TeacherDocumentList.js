import React, { useEffect, useState } from "react";
import { Button, Col, Container, Form, Row } from "react-bootstrap";
import { addTeacherDocument, getTeacherDocuments } from "../http/teacherDocumentAPI";
import { getCourses } from "../http/courseAPI";

function dateRangeOverlaps(a_start, a_end, b_start, b_end) {
    if (a_start <= b_start && b_start <= a_end) return true; // b starts in a
    if (a_start <= b_end && b_end <= a_end) return true; // b ends in a
    if (b_start < a_start && a_end < b_end) return true; // a in b
    return false;
}

export default function TeacherDocumentList({ teacherId }) {
    const [teacherDocuments, setTeacherDocuments] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [from, setFrom] = useState('');
    const [to, setTo] = useState('');
    const [courses, setCourses] = useState([]);
    const [selectedCourseId, setSelectedCourseId] = useState(null);

    useEffect(() => {
        getTeacherDocuments(teacherId).then((teacherDocuments) => {
            setTeacherDocuments(teacherDocuments.sort(function (a, b) {
                return new Date(b.date) - new Date(a.date) || b.number - a.number;
            }));
            setIsLoaded(true);
        })
    }, [teacherId]);

    useEffect(() => {
        getCourses().then((courses) => {
            setCourses(courses)
        })
    }, [])
    if (!isLoaded) {
        return <div />
    }

    const filteredTeacherDocuments = teacherDocuments.filter(teacherDocument =>
        dateRangeOverlaps(
            from ? new Date(from).getTime() : -Infinity,
            to ? new Date(to).getTime() : Infinity,
            new Date(teacherDocument.start).getTime(),
            new Date(teacherDocument.end).getTime())
    )

    const onSubmit = (e) => {
        e.preventDefault();
        addTeacherDocument({
            teacher: { id: teacherId },
            course: { id: selectedCourseId },
        }).then(teacherDocument => setTeacherDocuments([teacherDocument, ...teacherDocuments]))
    }

    return (
        <Container className='col-md'>
            <h3 className='mt-4'>Schedule</h3>
            <Form className="d-flex">

                <Form.Group className="mb-3 mx-2" >
                    <Form.Label>From</Form.Label>
                    <Form.Control type="date" style={{ width: '200px' }} value={from} onChange={e => setFrom(e.target.value)} />
                </Form.Group>
                <Form.Group className="mb-3" >
                    <Form.Label>To</Form.Label>
                    <Form.Control type="date" style={{ width: '200px' }} value={to} onChange={e => setTo(e.target.value)} />
                </Form.Group>

            </Form>
            <div className='w-100 p-3 d-flex'>
                <Container className='ms-3 '>
                    <Row>
                        <Col>
                            <b>
                                Name
                            </b>
                        </Col>
                        <Col>
                            <b>
                                Start
                            </b>
                        </Col>

                        <Col>
                            <b>
                                End
                            </b>
                        </Col>

                    </Row>
                </Container>

            </div>
            {
                filteredTeacherDocuments.map((teacherDocument, index) => {
                    return <div key={teacherDocument.id} className='w-100 p-3 d-flex'
                        style={{ background: index % 2 ? '#edf4f6' : 'white' }}>
                        <Container className='ms-3'>
                            <Row>
                                <Col>
                                    <b>
                                        {teacherDocument.course?.name ?? ''}
                                    </b>
                                </Col>
                                <Col>
                                    {new Date(teacherDocument.start).toLocaleDateString()}
                                </Col>

                                <Col>
                                    {new Date(teacherDocument.end).toLocaleDateString()}
                                </Col>

                            </Row>
                        </Container>

                    </div>
                })
            }
            {
                filteredTeacherDocuments?.length === 0 &&
                <p>Documents not found</p>
            }

            <Form className="d-flex mt-4 align-items-end" onSubmit={onSubmit}>
                <Form.Group >
                    <Form.Label>Course</Form.Label>
                    <Form.Select
                        style={{ width: '200px' }}
                        value={selectedCourseId}
                        onChange={e => setSelectedCourseId(+e.target.value)}
                        placeholder="choose course"
                    >
                        <option> select value</option>
                        {
                            courses.map((course) => (
                                <option key={course.id} value={course.id} >{course.name}</option>
                            ))
                        }
                    </Form.Select>
                </Form.Group>
                <Button className="mx-4" type="submit" disabled={selectedCourseId == null}>Add for period</Button>
            </Form>
        </Container>
    )
}
