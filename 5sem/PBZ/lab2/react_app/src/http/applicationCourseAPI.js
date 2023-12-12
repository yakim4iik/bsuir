import {$host} from '.';

export async function getApplicationCourses(applicationId) {
    const { data } = await $host.get('/api/application-course', { params: { applicationId } });
    return data;
}

export async function getActualStudentsNumber(courseId, from, to) {
    const { data } = await $host.get('/api/application-course/number', { params: { courseId, from, to } });
    return data;
}

export async function updateApplicationCourse(applicationCourse) {
    await $host.put(
        '/api/application-course',
        applicationCourse
    );
}

export async function addApplicationCourse(applicationCourse) {
    const { data } = await $host.post(
        '/api/application-course',
        applicationCourse
    );
    return data;
}

export async function removeApplicationCourse(applicationCourse) {
    await $host.delete(
        '/api/application-course', {data: applicationCourse}
        // { params: { 
        //     courseId: applicationCourse.applicationCourseId.course.id,
        //     employeeId: applicationCourse.applicationCourseId.employee.id,
        //     applicationId: applicationCourse.applicationCourseId.application.id,
        //   } 
        // }

    );
}
