package com.example.demo.repositories;


import com.example.demo.models.Application;

import org.springframework.data.repository.CrudRepository;

public interface ApplicationRepository extends CrudRepository<Application, Long> {
}
