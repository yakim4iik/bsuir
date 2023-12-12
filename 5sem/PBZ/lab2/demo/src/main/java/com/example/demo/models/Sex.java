package com.example.demo.models;

import jakarta.persistence.Entity;

@Entity
public class Sex extends NamedEntity {
    public enum Values {
        MALE(1L),
        FEMALE(2L);

        private Long id;

        Values(final Long id) {
            this.id = id;
        }

        public Long getId() {
            return id;
        }
    }
}
