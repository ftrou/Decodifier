from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

from .config import DEFAULT_IGNORE


class Project(BaseModel):
    id: str
    name: str
    path: str
    ignore: List[str] = Field(default_factory=lambda: list(DEFAULT_IGNORE))
    created_at: Optional[str] = None
    notes: List[str] = Field(default_factory=list)
    packs: List[str] = Field(default_factory=list)


class ProjectCreate(BaseModel):
    name: str
    path: str
    ignore: List[str] = Field(default_factory=list)


class PackInstallPayload(BaseModel):
    path: str
    name: Optional[str] = None
    overwrite: bool = False


class ProjectPacksPayload(BaseModel):
    packs: List[str]

class SearchRequest(BaseModel):
    project_id: str
    query: str
    k: int = 12


class SearchResult(BaseModel):
    text: str
    meta: Dict[str, Any] = Field(default_factory=dict)


class SearchResponse(BaseModel):
    results: List[SearchResult] = Field(default_factory=list)


class FilePayload(BaseModel):
    path: str
    content: str


class PatchPayload(BaseModel):
    path: str
    patch: str


class NotesPayload(BaseModel):
    notes: List[str]


class Conversation(BaseModel):
    id: str
    title: str
    messages: List[Dict[str, Any]] = Field(default_factory=list)


class ConversationState(BaseModel):
    conversations: List[Conversation] = Field(default_factory=list)
    active_id: Optional[str] = None


class ConversationCreate(BaseModel):
    id: str
    title: str


class ConversationAppend(BaseModel):
    id: str
    title: Optional[str] = None
    message: Dict[str, Any]


class ActiveConversationPayload(BaseModel):
    id: str
