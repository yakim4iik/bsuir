import { $host } from '.';

export async function getEmployees(organizationId) {
    const { data } = await $host.get('/api/employee', { params: { organizationId: organizationId } });
    return data;
}

export async function updateEmployee(employee) {
    await $host.put(
        '/api/employee',
        employee
    );
}

export async function addEmployee(employee) {
    const { data } = await $host.post(
        '/api/employee',
        employee
    );
    return data;
}

export async function removeEmployee(employee) {
    await $host.delete(
        '/api/employee',
        { params: { employeeId: employee.id } }
    );
}
