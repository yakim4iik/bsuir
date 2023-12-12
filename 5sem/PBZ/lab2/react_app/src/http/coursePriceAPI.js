import { $host } from '.';

export async function getCoursePrices(courseId) {
    const { data } = await $host.get('/api/course-price', { params: { courseId } });
    return data;
}

export async function updateCoursePrice(coursePrice) {
    await $host.put(
        '/api/course-price',
        coursePrice
    );
}

export async function addCoursePrice(coursePrice) {
    const { data } = await $host.post(
        '/api/course-price',
        coursePrice
    );
    return data;
}

export async function removeCoursePrice(coursePrice) {
    await $host.delete(
        '/api/course-price',
        { params: { coursePriceId: coursePrice.id } }
    );
}
