package com.onrender.homepick.repository;

import com.onrender.homepick.dto.MemberJoinDto;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public class MemberRepository{

    private final JdbcTemplate jdbcTemplate;

    public MemberRepository(JdbcTemplate jdbcTemplate){
        this.jdbcTemplate = jdbcTemplate;
    }

    private final RowMapper<MemberJoinDto> rowMapper = (rs, rowNum) -> {
        MemberJoinDto dto = new MemberJoinDto();
        dto.setUsername(rs.getString("username"));
        dto.setPassword(rs.getString("password"));
        dto.setName(rs.getString("name"));
        dto.setEmail(rs.getString("email"));
        return dto;
    };

    // 아이디로 회원 정보 조회 (로그인용)
    public Optional<MemberJoinDto> findByUsername(String username){
        String sql = "SELECT * FROM member WHERE username = ?";
        return jdbcTemplate.query(sql, rowMapper, username).stream().findFirst();
    }

    public void save(MemberJoinDto dto){
        String sql = "INSERT INTO member (username, password, name, email, role) VALUES (?, ?, ?, ?, 'ROLE_USER')";
        jdbcTemplate.update(sql, dto.getUsername(), dto.getPassword(), dto.getName(), dto.getEmail());
    }

    public boolean existsByUsername(String username){
        String sql = "SELECT COUNT(*) FROM member WHERE username = ?";
        Integer count = jdbcTemplate.queryForObject(sql, Integer.class, username);
        return count != null && count > 0;
    }
}