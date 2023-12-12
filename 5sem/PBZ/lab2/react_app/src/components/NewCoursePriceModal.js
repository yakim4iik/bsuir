import React, { useState } from "react";
import { Button, Form, Modal } from "react-bootstrap"
import { addCoursePrice } from "../http/coursePriceAPI";


function NewCoursePriceModal({ courseId, setCoursePriceList, show, onHide, fetchCourse }) {
    const [number, setNumber] = useState('');
    const [price, setPrice] = useState('');

    function newCoursePrice() {
        addCoursePrice({ course: { id: courseId }, number, price }).then(newItem => {
            setCoursePriceList(list => [newItem, ...list]);
            fetchCourse();
            onHide();
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
                    Price Change
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group className="mb-3" >
                        <Form.Label>Number</Form.Label>
                        <Form.Control type="number" value={number} onChange={e => setNumber(e.target.value)} />
                    </Form.Group>
                    <Form.Group className="mb-3" >
                        <Form.Label>Price</Form.Label>
                        <Form.Control type="number" value={price} onChange={e => setPrice(e.target.value)} />
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button onClick={newCoursePrice}>Set</Button>
            </Modal.Footer>
        </Modal>
    )
}

export default NewCoursePriceModal