# Welcome to My Vector DB
***

## Task
TODO - What is the problem? And where is the challenge?

## Description
System to store, manage, and query high-dimensional vectors
General steps:
1. Understand requirements
   1. Task Objective: Build a hybrid vector db combining KD-Trees and LSH for efficient similarity search in high-dimensional space
   2. Use Case: Multimedia content search and retrieval (e.g. image/audio similarity, recommendation engines)
   3. Core Features:
      1. Store high-dimensional vectors with metadata
      2. Perform nearest-neighbor queries quickly
      3. Support distributed and resilient architectures for scalability

2. Data Ingestion
   1. Input Constraints
      1. Vectors must have a fixed length
      2. Vectors must be normalized (e.g. to unit length)
      3. Embedding Generation
         1. Use a pre-trained embedding model (e.g. PyTorch for deep learning embeddings)
         2. Example: Convert images into feature vectors using models like ResNet

3. Data Storage
   1. Hybrid Storage:
      1. Use KD-Trees for partitioning the space into manageable regions
      2. Use LSH for hashing similar vectors into buckets for approximate seach
   2. Persistent Storage
      1. Store metadata and embeddings in FoundationDB for durability and distributed access

4. Indexing
   1. Tree-Based Indexing (KD-Trees):
      1. Use KD-Trees to partition the vector space hierarchically
      2. e.g. SciPy KDTree
   2. Hash-Based Indexing (LSH)
      1. Hash similar vectors into the same bucket
      2. e.g. Use a library like FAISS or implement custom LSH functions for approximate nearest neighbor (ANN) search
   3. Combined Use
      1. Use KD-Trees for initial space partitioning
      2. Within each partition, use LSH to bucket similar vectors and retrieve them quickly

5. Querying
   1. Similarity Search: Use cosine similarity or Euclidean distance to compare vectors
   2. Top-K Retrieval: Retrieve the k most similar vectors based on similarity score
   3. Metadata Filtering: Add filters for metadata constraints (e.g. vector tags, labels)

6. Implement CRUD Operations
      1. Add: Insert new vectors into the KD-Tree and LSH buckets
      2. Get: Retrieve vectors or metadata by ID
      3. Delete: Remove vectors from both the KD-Tree and LSH buckets
      4. Update: Modify vector metadata or re-index vectors

7. Optimize for Scale
   1. Sharding
      1. Distribute KD-Tree partitions and LSH buckets across multiple searvers for load balancing
      2. Use metadata to determine which shard stores a specific vector
   2. Distributed Systems
      1. Use Docker and Kubernetes to deploy the system across a cluster
      2. Leverage FoundationDB for distributed metadata storage
8. Build a Query Interface
9. Persistence and Resilience
10. Test and Validate
11. Extend with Advanced Features
12. Monitor and Maintain
   

   Datastructures used for the vector db
   db operations
   explain choices
   why different from relational and noSQL db
   duckdb
   minimal db operations
   simple, but follows the principles
   showcase how it works; use cases, scenarios; we can create our own data; looking for the concepts
   

## Installation
TODO - How to install your project? npm install? make? make re?

## Usage
TODO - How does it work?
```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
