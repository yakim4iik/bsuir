import React, { useEffect, useState, useCallback } from "react";
import { Button, Container, Form } from "react-bootstrap";
import { addCourse, getCourses, updateCourse } from "../http/courseAPI";
import { useNavigate, useParams, useLocation } from "react-router-dom";
import { COURSE_PATH } from "../utils/paths";
import { getTypes } from "../http/typeAPI";
import CoursePriceList from "../components/CoursePriceList";
import { getActualStudentsNumber } from "../http/applicationCourseAPI";
import { getFio } from "../utils/formMessage";

export default function Course() {
    const params = useParams();
    const navigate = useNavigate();
    const location = useLocation();

    const courseId = +params.id;
    const isCreateCourse = params.id === undefined;
    const [course, setCourse] = useState(null);
    const [types, setTypes] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [from, setFrom] = useState(null);
    const [to, setTo] = useState(null);

    const [code, setCode] = useState('');
    const [name, setName] = useState('');
    const [typeId, setTypeId] = useState('');
    const [days, setDays] = useState('');
    const [students, setStudents] = useState('');

    const [actualStudents, setActualStudents] = useState('');

    const fetchCourse = useCallback(() => getCourses().then((courses) => {
        const result = courses.find((course) => courseId === course.id)
        if (result) {
            setCourse(result);
            setTypeId(result.type?.id)
            setDays(result.days);
            setStudents(result.students);
        }
        setIsLoaded(true);
    }), [courseId]);

    useEffect(() => {
        getTypes().then(data => setTypes(data))
        if (isCreateCourse) {
            setIsLoaded(true);
            return;
        }
        fetchCourse()
    }, [fetchCourse, isCreateCourse]);

    const onSubmit = (event) => {
        event.preventDefault();
        const body = { ...course, days, students, type: { id: typeId } }
        if (isCreateCourse) {
            body.code = code
            body.name = name
            body.type = { id: typeId }
            body.organization = { id: location.state.organizationId }
            addCourse(body).then(id => {
                setIsLoaded(false);
                navigate(COURSE_PATH + id)
            })
        } else {
            updateCourse(body)
        }
    }

    const findNumber = (event) => {
        event.preventDefault();
        if (!from || !to) {
            setActualStudents('')
        } else {
            getActualStudentsNumber(courseId, from, to).then(result => {
                if (!result || result.length === 0) {
                    setActualStudents('Teacher periods not found')
                } else {
                    let resultString = ''
                    for (let item of result) {
                        resultString += new Date(item.start).toLocaleDateString() + ' - '
                            + new Date(item.end).toLocaleDateString() + ' Students: '
                            + item.students
                            + '\n'
                    }
                    setActualStudents(resultString)
                }
            })
        }
    }

    if (!isLoaded) {
        return <div />
    }
    if (!course && !isCreateCourse) {
        return <p className='error-not-found'>Not found</p>;
    }

    return (
        <Container className='col-md'>
            {
                isCreateCourse ?
                    <h3 className='mt-3'>New course</h3> :
                    <h3 className='mt-3'>Course {course.code || '№' + course.id}, {course.name}</h3>
            }
            <Form onSubmit={onSubmit}>
                {
                    isCreateCourse && <>
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
                    <Form.Label>Type</Form.Label>
                    <Form.Select
                        style={{ width: '200px' }}
                        value={typeId}
                        onChange={e => setTypeId(e.target.value)}
                    >
                        <option> select value</option>

                        {
                            types.map((type) => (
                                <option key={type.id} value={type.id} >{type.name}</option>
                            ))
                        }
                    </Form.Select>
                </Form.Group>
                <Form.Group className="mb-3" >
                    <Form.Label>Days</Form.Label>
                    <Form.Control type="number" style={{ width: '200px' }} value={days} onChange={e => setDays(e.target.value)} />
                </Form.Group>
                <Form.Group className="mb-3" >
                    <Form.Label>Students</Form.Label>
                    <Form.Control type="number" style={{ width: '200px' }} value={students} onChange={e => setStudents(e.target.value)} />
                </Form.Group>

                <Button type="submit">{isCreateCourse ? 'Create' : 'Update'}</Button>
            </Form>

            {
                !isCreateCourse &&
                <>
                    <p className="mt-3 h5">Current teacher:  {course.teacher ? getFio(course.teacher) : '-'} </p>
                    <p className="h5">Current price:  {course.price ?? '-'} </p>
                    <p className="h5">Price with NDS: {course.priceNds ?? '-'}</p>

                    <CoursePriceList courseId={courseId} fetchCourse={fetchCourse} />
                    <Form className="d-flex align-items-end mt-4 mb-3" onSubmit={findNumber}>
                        <Form.Group >
                            <Form.Label>From</Form.Label>
                            <Form.Control type="date" value={from} onChange={e => setFrom(e.target.value)} />
                        </Form.Group>

                        <Form.Group className="mx-3" >
                            <Form.Label>To </Form.Label>
                            <Form.Control type="date" value={to} onChange={e => setTo(e.target.value)} />
                        </Form.Group>

                        <Button type="submit">Find</Button>
                    </Form>

                    <p><strong>Students number and course dates:</strong></p>
                    <span style={{ whiteSpace: 'pre' }}>
                        {actualStudents}
                    </span>

                </>
            }

        </Container>
    )
}
