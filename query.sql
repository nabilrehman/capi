WITH
  UserLolComments AS (
    SELECT
      pq.title AS question_title,
      u.display_name,
      COUNT(c.id) AS lol_comment_count
    FROM `bq-demos-469816.stackoverflow2.posts_questions` AS pq
    INNER JOIN `bq-demos-469816.stackoverflow2.comments` AS c
      ON pq.id = c.post_id
    INNER JOIN `bq-demos-469816.stackoverflow2.users` AS u
      ON c.user_id = u.id
    WHERE LOWER(c.text) LIKE '%lol%'
    GROUP BY pq.title, u.display_name
  ),
  RankedUserLolComments AS (
    SELECT
      question_title,
      display_name,
      lol_comment_count,
      ROW_NUMBER()
        OVER (PARTITION BY question_title ORDER BY lol_comment_count DESC) AS rn
    FROM UserLolComments
  )
SELECT question_title, display_name, lol_comment_count
FROM RankedUserLolComments
WHERE rn <= 5
ORDER BY question_title, lol_comment_count DESC;