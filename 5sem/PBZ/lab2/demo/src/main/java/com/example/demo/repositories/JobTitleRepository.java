package com.example.demo.repositories;


import com.example.demo.models.JobTitle;

import org.springframework.data.repository.CrudRepository;

public interface JobTitleRepository extends CrudRepository<JobTitle, Long> {
}
