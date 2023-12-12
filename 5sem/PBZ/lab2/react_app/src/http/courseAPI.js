import { $host } from '.';

export async function getCourses(organizationId, historyDate) {
    const { data } = await $host.get('/api/course', { params: { organizationId, historyDate: historyDate ? historyDate : null } });
    return data;
}

export async function updateCourse(course) {
    await $host.put(
        '/api/course',
        course
    );
}

export async function addCourse(course) {
    const { data } = await $host.post(
        '/api/course',
        course
    );
    return data;
}

export async function removeCourse(course) {
    await $host.delete(
        '/api/course',
        { params: { courseId: course.id } }
    );
}
