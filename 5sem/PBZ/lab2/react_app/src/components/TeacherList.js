import React, { useEffect, useState } from "react";
import { Button, Col, Container, Row } from "react-bootstrap";
import { getTeachers, removeTeacher } from "../http/teacherAPI";
import { useNavigate } from "react-router-dom";
import { TEACHER_PATH } from "../utils/paths";
import { ReactComponent as Cross } from '../img/cross.svg';
import { getFio } from "../utils/formMessage";

export default function TeacherList() {
    const [teachers, setTeachers] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    useEffect(() => {
        getTeachers().then((complaints) => {
            setTeachers(complaints);
            setIsLoaded(true);
        })
    }, []);
    const navigate = useNavigate();
    if (!isLoaded) {
        return <div />
    }

    const onDeleteTeacher = (teacher, index) => {
        removeTeacher(teacher)
        const updatedTeachers = [...teachers]
        updatedTeachers.splice(index, 1)
        setTeachers(updatedTeachers);
    }

    return (
        <Container className='col-md'>
            <h3 className='mt-4'>Teachers</h3>
            {
                teachers.map((teacher, index) => {
                    return <div key={teacher.id} className='w-100 p-3 d-flex'
                        style={{ background: index % 2 ? '#edf4f6' : 'white' }}>
                        <Container className='ms-3 clickable' onClick={() => navigate(TEACHER_PATH + teacher.id)}>
                            <Row>
                                <Col>
                                    {getFio(teacher)}
                                </Col>
                                <Col>
                                    {teacher.sex?.name ?? ''}
                                </Col>

                                <Col>
                                    {teacher.education?.name ?? ''}
                                </Col>

                                <Col>
                                    {new Date(teacher.birthday).toLocaleDateString()}
                                </Col>

                                <Col>
                                    {teacher.category?.name ?? ''}
                                </Col>

                                <Col>
                                    <button onClick={(e) => {
                                        e.stopPropagation();
                                        onDeleteTeacher(teacher, index)
                                    }}><Cross /></button>
                                </Col>

                            </Row>
                        </Container>
                    </div>
                })
            }
            <Button className="mt-4" type="submit" onClick={() => navigate(TEACHER_PATH)}>Add</Button>
        </Container>
    )
}
