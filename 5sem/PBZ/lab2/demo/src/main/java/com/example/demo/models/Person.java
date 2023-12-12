package com.example.demo.models;

import jakarta.persistence.*;
import java.io.Serializable;

@MappedSuperclass
public class Person implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID", unique = true, nullable = false, insertable = true, updatable = false)
    private Long id;

    @Column
    private String firstName;

    @Column
    private String surname;

    @Column
    private String middleName;

    
    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(final String firstName) {
        this.firstName = firstName.trim();
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(final String lastName) {
        this.surname = lastName.trim();
    }

    public String getMiddleName() {
        return middleName;
    }

    public void setMiddleName(final String middleName) {
        if (middleName != null)
            this.middleName = middleName.trim();
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }
}
