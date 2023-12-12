package com.example.demo.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;

@Entity
public class Organization extends NamedEntity {
    @Column
    private String code;

    @Column
    private String phone;

    @Column
    private String email;

    @Column
    private String address;

    // @OneToMany(mappedBy = "organization")
    // private Set<Application> applications;

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    // public Set<Application> getApplications() {
    //     return applications;
    // }

    // public void setApplications(Set<Application> applicationList) {
    //     this.applications = applicationList;
    // }

}
