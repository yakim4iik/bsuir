import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { ORGANIZATION_PATH, COURSE_PATH, TEACHER_PATH, APPLICATION_PATH } from '../utils/paths';
import { observer } from 'mobx-react-lite';
import Organization from '../pages/Organization';
import Course from '../pages/Course';
import MainPage from '../pages/MainPage';
import Teacher from '../pages/Teacher';
import Application from '../pages/Application';

function AppRouter() {
    return (
        <Routes>
            <Route path={'/'} element={<MainPage />} exact />

            <Route path={TEACHER_PATH} element={<Teacher />} />
            <Route path={TEACHER_PATH + ':id'} element={<Teacher />} />

            <Route path={APPLICATION_PATH} element={<Application />} />
            <Route path={APPLICATION_PATH + ':id'} element={<Application />} exact />

            <Route path={ORGANIZATION_PATH} element={<Organization />} />
            <Route path={ORGANIZATION_PATH + ':id'} element={<Organization />} />
            <Route path={COURSE_PATH} element={<Course />} />
            <Route path={COURSE_PATH + ':id'} element={<Course />} exact />


            <Route path='*' element={<p className='error-not-found'>Error 404. Wrong path</p>} />
        </Routes>
    )
}

export default observer(AppRouter);