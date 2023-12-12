import {$host} from '.';

export async function getApplications(organizationId) {
    const { data } = await $host.get('/api/application', { params: { organizationId: organizationId } });
    return data;
}

export async function updateApplication(application) {
    await $host.put(
        '/api/application',
        application
    );
}

export async function addApplication(application) {
    const { data } = await $host.post(
        '/api/application',
        application
    );
    return data;
}

export async function removeApplication(application) {
    await $host.delete(
        '/api/application',
        { params: { applicationId: application.id } }
    );
}
