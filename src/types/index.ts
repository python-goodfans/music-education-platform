// src/types/index.ts

export interface Subject {
    id: number;
    name: string;
    description?: string;
}

export interface Article {
    id: number;
    title: string;
    content: string;
    authorId: number;
    subjectId: number;
    publishedAt?: Date;
}

export interface Competition {
    id: number;
    name: string;
    date: Date;
    location: string;
}

export interface Activity {
    id: number;
    name: string;
    type: string;
    requiredMaterials?: string[];
}