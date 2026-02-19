-- Схема для мониторинга событий приложения
CREATE TABLE IF NOT EXISTS app_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Тестовые данные
INSERT INTO app_events (event_type, description) VALUES 
('SYSTEM_START', 'Приложение запущено в Docker контейнере'),
('DB_INIT', 'Первичная инициализация схемы данных');