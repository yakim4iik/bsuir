package com.example.demo.models;

import jakarta.persistence.Column;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.MappedSuperclass;
import java.io.Serializable;
import java.util.Objects;

@MappedSuperclass
public abstract class NamedEntity implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID", unique = true, nullable = false, insertable = true, updatable = false)
    private Long id;

    @Column(name = "NAME", nullable = false, insertable = true, updatable = true)
    private String name;

    public NamedEntity() {
        this(null);
    }


    public NamedEntity(final Long id) {
        this.id = id;
    }
    
    public Long getId() {
        return id;
    }


    public String getName() {
        return name;
    }

    public void setName(final String name) {
        this.name = name.trim();
    }

    @Override
    public boolean equals(Object o) {
        if (!super.equals(o)) {
            return false;
        }

        NamedEntity obj = (NamedEntity) o;
        return name.equals(obj.getName());

    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}
