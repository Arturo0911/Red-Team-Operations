package com.bmdyy.bluebird.model;

public class User {
   private Long id;
   private String username;
   private String password;
   private String email;
   private String name;
   private String description;

   public User(Long id, String username, String password, String email, String name, String description) {
      this.id = id;
      this.username = username;
      this.password = password;
      this.email = email;
      this.name = name;
   }

   public User() {
   }

   public Long getId() {
      return this.id;
   }

   public String getUsername() {
      return this.username;
   }

   public String getPassword() {
      return this.password;
   }

   public String getEmail() {
      return this.email;
   }

   public String getName() {
      return this.name;
   }

   public String getDescription() {
      return this.description;
   }

   public void setId(Long id) {
      this.id = id;
   }

   public void setUsername(String username) {
      this.username = username;
   }

   public void setPassword(String password) {
      this.password = password;
   }

   public void setEmail(String email) {
      this.email = email;
   }

   public void setName(String name) {
      this.name = name;
   }

   public void setDescription(String description) {
      this.description = description;
   }
}
