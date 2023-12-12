package com.example.demo.repositories;


import com.example.demo.models.Sex;

import org.springframework.data.repository.CrudRepository;

public interface SexRepository extends CrudRepository<Sex, Long> {
}
