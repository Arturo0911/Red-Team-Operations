package com.bmdyy.bluebird.model;

import java.sql.Timestamp;

public class Post {
   private int id;
   private String text;
   private int authorId;
   private Timestamp postedAt;

   public Post(int id, String text, int authorId, Timestamp postedAt) {
      this.id = id;
      this.text = text;
      this.authorId = authorId;
      this.postedAt = postedAt;
   }

   public Post() {
   }

   public int getId() {
      return this.id;
   }

   public String getText() {
      return this.text;
   }

   public int getAuthorId() {
      return this.authorId;
   }

   public Timestamp getPostedAt() {
      return this.postedAt;
   }

   public void setId(int id) {
      this.id = id;
   }

   public void setText(String text) {
      this.text = text;
   }

   public void setAuthorId(int authorId) {
      this.authorId = authorId;
   }

   public void setPostedAt(Timestamp postedAt) {
      this.postedAt = postedAt;
   }
}
