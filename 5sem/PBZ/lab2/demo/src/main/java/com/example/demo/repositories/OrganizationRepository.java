package com.example.demo.repositories;


import com.example.demo.models.Organization;

import org.springframework.data.repository.CrudRepository;

public interface OrganizationRepository extends CrudRepository<Organization, Long> {
}
