package com.onrender.homepick.repository;

import com.onrender.homepick.dto.QnaDto;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class QnaRepository{

    private final JdbcTemplate jdbcTemplate;

    public QnaRepository(JdbcTemplate jdbcTemplate){
        this.jdbcTemplate = jdbcTemplate;
    }

    private final RowMapper<QnaDto> rowMapper = (rs, rowNum) -> {
        QnaDto qna = new QnaDto();
        qna.setId(rs.getLong("id"));
        qna.setTitle(rs.getString("title"));
        qna.setContent(rs.getString("content"));
        qna.setWriter(rs.getString("writer"));
        qna.setStatus(rs.getString("status"));
        qna.setCreatedAt(rs.getTimestamp("created_at").toLocalDateTime());
        return qna;
    };

    // 전체 QnA 목록 조회 (최신순)
    public List<QnaDto> findAll(){
        String sql = "SELECT * FROM qna ORDER BY id ASC";
        return jdbcTemplate.query(sql, rowMapper);
    }

    // 질문 등록
    public void save(QnaDto qna){
        String sql = "INSERT INTO qna (title, content, writer, status) VALUES (?, ?, ?, '대기중')";
        jdbcTemplate.update(sql, qna.getTitle(), qna.getContent(), qna.getWriter());
    }
}
