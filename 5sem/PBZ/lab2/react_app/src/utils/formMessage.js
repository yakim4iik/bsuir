
export function getFio(person) {
    let name = person.firstName + ' ';
    if (person.middleName) {
        name += person.middleName + ' ';
    }
    name += person.surname;
    return name;
}
