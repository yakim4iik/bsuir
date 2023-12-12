import { $host } from '.';

export async function getOrganizations() {
    const { data } = await $host.get('/api/organization');
    return data;
}

export async function updateOrganization(organization) {
    await $host.put(
        '/api/organization',
        organization
    );
}

export async function addOrganization(organization) {
    const { data } = await $host.post(
        '/api/organization',
        organization
    );
    return data;
}

export async function removeOrganization(organization) {
    await $host.delete(
        '/api/organization',
        {params: { organizationId: organization.id }}
    );
}
