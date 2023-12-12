import React, { useEffect, useState } from "react";
import { Button, Col, Container, Row } from "react-bootstrap";
import { getCoursePrices } from "../http/coursePriceAPI";
import { useNavigate } from "react-router-dom";
import { COURSE_PATH } from "../utils/paths";
import NewCoursePriceModal from "./NewCoursePriceModal";

export default function CoursePriceList({ courseId, fetchCourse }) {
    const [coursePrices, setCoursePrices] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [isEdit, setIsEdit] = useState(false);
    useEffect(() => {
        getCoursePrices(courseId).then((coursePrices) => {
            setCoursePrices(coursePrices.sort(function(a,b){
                return new Date(b.date) - new Date(a.date) || b.number - a.number;
              }));
            setIsLoaded(true);
        })
    }, [courseId]);
    const navigate = useNavigate();
    if (!isLoaded) {
        return <div />
    }
    return (
        <Container className='col-md'>
            <h3 className='mt-4'>CoursePrices</h3>
            <div className='w-100 p-3 d-flex'>
                <Container className='ms-3 '>
                    <Row>
                        <Col md='auto'>
                            <b>
                                Number
                            </b>
                        </Col>
                        <Col>
                            <b>
                                Date
                            </b>
                        </Col>

                        <Col>
                            <b>
                                Price
                            </b>
                        </Col>

                    </Row>
                </Container>

            </div>
            {
                coursePrices.map((coursePrice, index) => {
                    return <div key={coursePrice.id} className='w-100 p-3 d-flex'
                        style={{ background: index % 2 ? '#edf4f6' : 'white' }}>
                        <Container className='ms-3 clickable' onClick={() => navigate(COURSE_PATH + coursePrice.id)}>
                            <Row>
                                <Col md='auto'>
                                    <b>
                                        {coursePrice.number}
                                    </b>
                                </Col>
                                <Col>
                                    {new Date(coursePrice.date).toLocaleDateString()}
                                </Col>

                                <Col>
                                    {coursePrice.price != null ? coursePrice.price : '-'}
                                </Col>

                            </Row>
                        </Container>


                    </div>
                })
            }
            <Button className="mt-4" type="submit" onClick={() => setIsEdit(true)}>Add</Button>
            <NewCoursePriceModal
                show={isEdit}
                courseId={courseId}
                setCoursePriceList={setCoursePrices}
                fetchCourse={fetchCourse}
                onHide={() => setIsEdit(false)}
            />
        </Container>
    )
}
