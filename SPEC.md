# Spec for the way this "Database" works
*Prediction for future self: This was a terrible idea*

## General Information
This document defines how this sytem works.
The way important information (Database metadata, Table metadata) is stored is via pinned messages in their respective channels (See section "Pin Messages")
An entire guild will be used for one system (See section "Structure of Guild")

## Structure of Guild
Categories in guilds are for Databases.
Each Database (Category) may hold up to 50 Tables (Channels).
Categories will be named to the name of the Database.
Within each Category, there may be up to 50 Tables (Channels).
Channels will be named to the name of the Table.
Within the Channels there will be messages representing records in the database

### Databases
Each Database is defined as a category in a discord guild. It may hold up to 50 Tables.
A Database is referenced by a name - names cannot be duplicated.
There is no pinned message for a Database table, the only data we need is its name and that's stored as the category name.

### Tables
Each Table is defined as a channel in a "Database" (Category). It has an unlimited amount of records (Messages), but there is a substantial performance drop off in chunks of 50 records.
A Table is referenced by a name - names cannot be duplicated.
The pinned message for a Table (Channel) is sent in the channel for that table and looks like the following:
```
0
field_name:field_name:field_name
```
The second line is a colon-seperated list of field names.

### Records
Each Record is defined by a message in a Table (Channel)
The structure of a Record (Message) is as follows:
```
field_value:field_value:field_value
```
The first line is a colon-seperated list of field values, which match up with the field names from the pinned message

### Pinned Messages
Pinned messages hold important metadata about a database or tables within that database.
Their structure is the following:
```
{pin_type_number}
[Rest of message is data]
```
pin_type number can be:
 - 0: This is for a table defenition

## Library Classes
### Record
`classes.record`
Represents a record in a table
Properties:
`record.table`: A Table object representing the Table this record belongs to
`record.created_at`: An ISO8601 timestamp of when the record was created
`record.updated_at`: An ISO8601 timestamp of when the record was updated.
`record.data`: A dictionary containing the data held in the record. Example: 
```
{
    "field_name_1": "field_value",
    "field_name_2": "second_field_value"
}
```
Methods:
`record.update_field("field_name", "new_field_value")`: Updates the specified field and sets it to the new value

### Table
`classes.table`
Represents a Table containing Records in a Database
