import { $host } from '.';

export async function getTeacherDocuments(teacherId) {
    const { data } = await $host.get('/api/teacher-document', { params: { teacherId }});
    return data;
}

export async function addTeacherDocument(teacherDocument) {
    const { data } = await $host.post(
        '/api/teacher-document',
        teacherDocument
    );
    return data;
}