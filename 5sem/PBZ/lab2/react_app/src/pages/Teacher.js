import React, { useEffect, useState } from "react";
import { Button, Container, Form } from "react-bootstrap";
import { addTeacher, getTeachers, updateTeacher } from "../http/teacherAPI";
import { useNavigate, useParams } from "react-router-dom";
import { getFio } from "../utils/formMessage";
import { ORGANIZATION_PATH, TEACHER_PATH } from "../utils/paths";
import TeacherDocumentList from "../components/TeacherDocumentList";

const sexValues = [{ id: 1, name: 'man' }, { id: 2, name: 'woman' }]
const educationValues = [{ id: 1, name: 'primary' }, { id: 2, name: 'secondary' }, { id: 3, name: 'higher' }]
const categoryValues = [{ id: 1, name: 'first' }, { id: 2, name: 'second' }, { id: 3, name: 'highest' }]

export default function Teacher() {
    const params = useParams();
    const navigate = useNavigate();

    const teacherId = +params.id;
    const isCreateTeacher = params.id === undefined;
    const [teacher, setTeacher] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);

    const [firstName, setFirstName] = useState('');
    const [middleName, setMiddleName] = useState('');
    const [surname, setSurname] = useState('');
    const [birthday, setBirthday] = useState('');
    const [sexId, setSexId] = useState();
    const [educationId, setEducationId] = useState();
    const [categoryId, setCategoryId] = useState();

    useEffect(() => {
        if (isCreateTeacher) {
            setIsLoaded(true);
            return;
        }
        getTeachers().then((teachers) => {
            const result = teachers.find((teacher) => teacherId === teacher.id)
            if (result) {
                setTeacher(result);
                setFirstName(result.firstName);
                setMiddleName(result.middleName);
                setSurname(result.surname);
                setBirthday(new Date(result.birthday).toISOString().substring(0, 10))
                setSexId(result.sex?.id)
                setEducationId(result.education?.id)
                setCategoryId(result.category?.id)
            }
            setIsLoaded(true);
        });

    }, [teacherId, isCreateTeacher]);

    const onSubmit = (event) => {
        event.preventDefault();
        const body = { ...teacher, firstName, middleName, surname, birthday }
        if (sexId != null) {
            body.sex = { id: sexId }
        }
        if (educationId != null) {
            body.education = { id: educationId }
        }
        if (categoryId != null) {
            body.category = { id: categoryId }
        }
        if (isCreateTeacher) {
            addTeacher(body).then(id => {
                setIsLoaded(false);
                navigate(TEACHER_PATH + id)
            })
        } else {
            updateTeacher(body)
        }
    }

    if (!isLoaded) {
        return <div />
    }
    if (!teacher && !isCreateTeacher) {
        return <p className='error-not-found'>Not found</p>;
    }

    return (
        <Container className='col-md'>
            {
                isCreateTeacher ?
                    <h3 className='mt-3'>New teacher</h3> :
                    <h3 className='mt-3'>Teacher {getFio(teacher)}</h3>
            }

            <Form onSubmit={onSubmit}>

                <Form.Group className="mb-3" >
                    <Form.Label>First Name</Form.Label>
                    <Form.Control type="text" placeholder="firstName" value={firstName} onChange={e => setFirstName(e.target.value)} />
                </Form.Group>

                <Form.Group className="mb-3" >
                    <Form.Label>Middle Name</Form.Label>
                    <Form.Control type="text" placeholder="middleName" value={middleName} onChange={e => setMiddleName(e.target.value)} />
                </Form.Group>

                <Form.Group className="mb-3" >
                    <Form.Label>Surname</Form.Label>
                    <Form.Control type="text" placeholder="surname" value={surname} onChange={e => setSurname(e.target.value)} />
                </Form.Group>

                <Form.Group className="mb-3" >
                    <Form.Label>Birthday</Form.Label>
                    <Form.Control type="date" placeholder="birthday" value={birthday} onChange={e => setBirthday(e.target.value)} />
                </Form.Group>

                <Form.Group className="mb-3" >
                    <Form.Label>Sex</Form.Label>
                    <Form.Select
                        style={{ width: '200px' }}
                        value={sexId}
                        onChange={e => setSexId(e.target.value)}
                    >
                        <option> select value</option>

                        {
                            sexValues.map((type) => (
                                <option key={type.id} value={type.id} >{type.name}</option>
                            ))
                        }
                    </Form.Select>
                </Form.Group>

                <Form.Group className="mb-3" >
                    <Form.Label>Education</Form.Label>
                    <Form.Select
                        style={{ width: '200px' }}
                        value={educationId}
                        onChange={e => setEducationId(e.target.value)}
                    >
                        <option> select value</option>
                        {
                            educationValues.map((type) => (
                                <option key={type.id} value={type.id} >{type.name}</option>
                            ))
                        }
                    </Form.Select>
                </Form.Group>

                <Form.Group className="mb-3" >
                    <Form.Label>Category</Form.Label>
                    <Form.Select
                        style={{ width: '200px' }}
                        value={categoryId}
                        onChange={e => setCategoryId(e.target.value)}
                    >
                        <option> select value</option>
                        {
                            categoryValues.map((type) => (
                                <option key={type.id} value={type.id} >{type.name}</option>
                            ))
                        }
                    </Form.Select>
                </Form.Group>

                <Button type="submit">{isCreateTeacher ? 'Create' : 'Update'}</Button>
            </Form>

            {
                !isCreateTeacher &&
                <TeacherDocumentList teacherId={teacherId} />
            }

        </Container>
    )
}
