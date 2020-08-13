# Databricks notebook source
# MAGIC %md 
# MAGIC # Welcome to the Wild West Hackathon
# MAGIC 
# MAGIC Thank you so much for your participation in this event.  We at Blueprint are so excited to have you here.  If you are reading this, then you are on a team participating in Challenge #1.  The goal of Challenge #1 will be to read in a stream of data and land it in Databricks Delta.  In this folder you will find a number of notebooks that will help you get started.  This is your team's folder.  You can create additional notebooks here as needed.  However, everything you create should be related to the competition.  No weirdly clever bitcoin mining notebooks please!  Also, things should be segmented in such a way that you won't be interfering with other teams.  This is a **friendly** competition, so please do not attempt to work around this segmentation to adversely affect other participants.
# MAGIC 
# MAGIC ### Challenge Details
# MAGIC 
# MAGIC You are a data engineer for a sporting goods store.  They want to send the data from their sales system to THE CLOUD.  A developer on the sales system has written an application to send real time data in addition to the initial load from the sales system to an **Azure Event Hub**.  Utilizing the **Capture** feature within Azure Event Hub, that data is being delivered directly to **Azure Data Lake Storage**.  Unfortunately, the raw data is not very useable.  It will be your job to *munge* the data into a useable format and land the data into **Databricks Delta** tables.  Once you have figured out how to work with the data, you will need to go a step further and make sure that the data in Delta is always kept up to date with something called **Structured Streaming**.  The streaming data is all either Inserts or Updates.  You won't have to worry about deletes, but you will need to **merge** updated records into the Delta tables to represent current state.
# MAGIC 
# MAGIC You have the choice of working in **Python** or **Scala** for this challenge.  One thing to keep in mind is that this is a *canned* hackathon.  We provide you with the starting point and also have a specific expectation of the ending point.  You are responsible for everything in between.  The starting point is the "Hackathon Start Up" notebook in either the Python or Scala folder.  The expectation for the ending point is streaming data into Delta tables created in the "Build Delta Tables" notebook.  In that notebook you will create the Database for your team, and the code for creating one of the tables is provided.  You will need to figure out the schemas for the remaining tables as part of the discovery process and populate the appropriate cells.
# MAGIC 
# MAGIC ### Help
# MAGIC 
# MAGIC We want this to be a fun and educational experience for everyone.  If can be difficult to find the fun when you get stuck, and when you are doing data engineering work, there are plenty of opportunities to get stuck.  While fighting through those challenges is often times the best way to learn, we don't want anyone to feel that they are too stuck to finish.  As such, help is available should you need it.  At the time of writing this, not all of the details have been finalized for getting help.  However, you can email me at dlokey@bpcs.com as needed.  I may not always be able to help right away, but I will try to get you moving in the right direction. 