import {$host} from '.';

export async function getTypes() {
    const {data} = await $host.get('/api/type');
    return data;
}


