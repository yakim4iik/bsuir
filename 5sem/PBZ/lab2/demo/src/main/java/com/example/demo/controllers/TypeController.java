package com.example.demo.controllers;


import com.example.demo.models.Type;
import com.example.demo.repositories.TypeRepository;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api/type")
public class TypeController {
    private final TypeRepository typeRepository;


    public TypeController(TypeRepository typeRepository) {
        this.typeRepository = typeRepository;
    }

    @GetMapping
    public Iterable<Type> getAll() {
        return typeRepository.findAll();
    }

}
