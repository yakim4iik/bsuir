package com.example.demo.controllers;


import com.example.demo.models.Organization;
import com.example.demo.repositories.OrganizationRepository;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api/organization")
public class OrganizationController {
    private final OrganizationRepository organizationRepository;

    public OrganizationController(OrganizationRepository organizationRepository) {
        this.organizationRepository = organizationRepository;
    }

    @GetMapping
    public Iterable<Organization> getAll() {
        return organizationRepository.findAll();
    }

    @PutMapping
    public void put(@RequestBody Organization organization) {
        organizationRepository.save(organization);
    }

    @PostMapping 
    public Long post(@RequestBody Organization organization) {
        organizationRepository.save(organization);
        return organization.getId();
    }

    @DeleteMapping
    public void delete(@RequestParam Long organizationId) {
        organizationRepository.deleteById(organizationId);
    }
}
