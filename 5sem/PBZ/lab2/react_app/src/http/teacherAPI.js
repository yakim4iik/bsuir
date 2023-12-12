import { $host } from '.';

export async function getTeachers() {
    const { data } = await $host.get('/api/teacher');
    return data;
}

export async function updateTeacher(teacher) {
    await $host.put(
        '/api/teacher',
        teacher
    );
}

export async function addTeacher(teacher) {
    const { data } = await $host.post(
        '/api/teacher',
        teacher
    );
    return data;
}

export async function removeTeacher(teacher) {
    await $host.delete(
        '/api/teacher',
        {params: { teacherId: teacher.id }}
    );
}
