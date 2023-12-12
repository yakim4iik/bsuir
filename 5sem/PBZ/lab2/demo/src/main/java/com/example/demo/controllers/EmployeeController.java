package com.example.demo.controllers;


import com.example.demo.models.Employee;
import com.example.demo.repositories.EmployeeRepository;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api/employee")
public class EmployeeController {
    private final EmployeeRepository employeeRepository;


    public EmployeeController(EmployeeRepository employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    @GetMapping
    public Iterable<Employee> getAll() {
        return employeeRepository.findAll();
    }

}
