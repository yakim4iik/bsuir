package com.example.demo.repositories;


import com.example.demo.models.Education;

import org.springframework.data.repository.CrudRepository;

public interface EducationRepository extends CrudRepository<Education, Long> {
}
