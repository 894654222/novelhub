"""Pending source changes that require admin approval."""

from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from .base import Base


class SourceChange(Base):
    __tablename__ = "source_changes"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    action = Column(String(16), nullable=False)  # 'create' or 'delete'
    source_id = Column(String, nullable=True)     # target source id for delete
    source_data = Column(JSONB, nullable=True)    # {id, name, url, plugin_name, config} for create
    status = Column(String(16), nullable=False, default="pending")  # pending, approved, rejected
    reviewer_id = Column(String, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    review_note = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    reviewed_at = Column(DateTime, nullable=True)
