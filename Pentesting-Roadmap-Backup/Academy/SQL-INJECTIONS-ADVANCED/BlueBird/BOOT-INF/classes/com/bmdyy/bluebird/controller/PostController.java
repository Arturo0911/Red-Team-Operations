package com.bmdyy.bluebird.controller;

import com.bmdyy.bluebird.security.services.UserDetailsImpl;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class PostController {
   @Autowired
   JdbcTemplate jdbcTemplate;

   @PostMapping({"/post"})
   public void createPost(@RequestParam String text, HttpServletResponse response) throws IOException {
      UserDetailsImpl userDetails = (UserDetailsImpl)SecurityContextHolder.getContext().getAuthentication().getPrincipal();
      if (text.length() <= 280) {
         String sql = "INSERT INTO posts (text, author_id, posted_at) VALUES (?, ?, CURRENT_TIMESTAMP);";
         this.jdbcTemplate.update(sql, new Object[]{text, userDetails.getId()});
      }

      response.sendRedirect("/");
   }
}
