import React, { useEffect, useState } from "react";
import { Button, Form, Modal } from "react-bootstrap"
import { getEmployees } from "../http/employeeAPI";
import { getCourses } from "../http/courseAPI";
import { addApplicationCourse } from "../http/applicationCourseAPI";
import { getApplications } from "../http/applicationAPI"


function NewApplicationCourseModal({ applicationId, applicationCourses, setApplicationCourses, show, onHide }) {
    const [employees, setEmployees] = useState([]);
    const [selectedEmployeeId, setSelectedEmployeeId] = useState(null);
    const [courses, setCourses] = useState([]);
    const [selectedCourseId, setSelectedCourseId] = useState(null);
    const [date, setDate] = useState('');


    const existingCourses = applicationCourses.filter(applicationCourse =>
        selectedEmployeeId && applicationCourse?.applicationCourseId?.employee?.id === selectedEmployeeId
    ).map(applicationCourse => applicationCourse?.applicationCourseId?.course?.id);
    const existingEmployees = applicationCourses.filter(applicationCourse =>
        selectedCourseId && applicationCourse?.applicationCourseId?.course?.id === selectedCourseId
    ).map(applicationCourse => applicationCourse?.applicationCourseId?.employee?.id);

    useEffect(() => {
        getEmployees().then((employees) => {
            setEmployees(employees);
        });
        getApplications().then(applications => {
            const application = applications.filter(item => item.id === applicationId)[0];
            if (application) {
                getCourses(application.organization.id).then((courses) => {
                    setCourses(courses)
                })
            }
        })
    }, [applicationId]);

    function newApplicationCourse() {
        if (selectedCourseId == null || selectedEmployeeId == null) {
            return
        }
        const applicationCourse = {
            applicationCourseId: {
                application: { id: applicationId },
                course: { id: selectedCourseId },
                employee: { id: selectedEmployeeId },
            },
            date,
        }
        addApplicationCourse(applicationCourse).then(() => {
            applicationCourse.applicationCourseId.course = courses.find(course => course.id === selectedCourseId)
            applicationCourse.applicationCourseId.employee = employees.find(employee => employee.id === selectedEmployeeId)
            applicationCourse.date = new Date(applicationCourse.date);
            setApplicationCourses([...applicationCourses, applicationCourse])
            onHide()
        })
    }

    return (
        <Modal
            show={show}
            onHide={onHide}
            centered
        >
            <Modal.Header closeButton>
                <Modal.Title id="contained-modal-title-vcenter">
                    Add Application Course
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group className="mb-3" >
                        <Form.Label>Employee</Form.Label>
                        <Form.Select
                            style={{ width: '200px' }}
                            value={selectedEmployeeId}
                            onChange={e => setSelectedEmployeeId(+e.target.value)}
                            placeholder="choose employee"
                        >
                            <option> select value</option>
                            {
                                employees.map((employee) => (
                                    <option key={employee.id} value={employee.id} disabled={existingEmployees.includes(employee.id)}>{employee.firstName + ' ' + employee.surname}</option>
                                ))
                            }
                        </Form.Select>
                    </Form.Group>
                    <Form.Group className="mb-3" >
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
                                    <option key={course.id} value={course.id} disabled={existingCourses.includes(course.id)}>{course.name}</option>
                                ))
                            }
                        </Form.Select>
                    </Form.Group>
                    <Form.Group className="mb-3" >
                        <Form.Label>Date</Form.Label>
                        <Form.Control type="date" value={date} onChange={e => setDate(e.target.value)} />
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button onClick={newApplicationCourse}>Set</Button>
            </Modal.Footer>
        </Modal>
    )
}

export default NewApplicationCourseModal