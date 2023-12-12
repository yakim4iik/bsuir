package com.example.demo.controllers;


import com.example.demo.models.Application;
import com.example.demo.repositories.ApplicationRepository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api/application")
public class ApplicationController {
    private final ApplicationRepository applicationRepository;


    public ApplicationController(ApplicationRepository applicationRepository) {
        this.applicationRepository = applicationRepository;
    }

    @GetMapping
    public Iterable<Application> getAll(Optional<Long> organizationId) {
        List<Application> applications = new ArrayList<>();
        for (Application application : applicationRepository.findAll()) {
            if (organizationId.isEmpty()) {
                applications.add(application);
                continue;
            }
            if (application.getOrganization() != null && organizationId.get().equals(application.getOrganization().getId())) {
                applications.add(application);
            }
        }
        return applications;
    }

     @PutMapping
    public void put(@RequestBody Application application) {

        applicationRepository.save(application);
    }

    @PostMapping
    public Long post(@RequestBody Application application) {
        applicationRepository.save(application);
        return application.getId();
    }

}
