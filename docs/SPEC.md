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
*The following section, as with the rest of this document, is still under development. Static properties may be changed to get_x() methods*
### Record
`classes.record`

Represents a record in a table

Properties:
 - `record.message`: A dict representing a Message object from the Discord API. Mainly for internal use.
 - `record.table`: A Table object representing the Table this record belongs to.
 - `record.created_at`: An ISO8601 timestamp of when the record was created.
 - `record.updated_at`: An ISO8601 timestamp of when the record was updated.
 - `record.data`: A dictionary containing the data held in the record. Example: 
```
{
    "field_name_1": "field_value",
    "field_name_2": "second_field_value"
}
```
Methods:
 - `record.update_field("field_name", "new_field_value")`: Updates the specified field and sets it to the new value. Returns the new Record instance for call chaining.
 - `record.delete()`: Deletes the Record Permanently.

### Table
`classes.table`

Represents a Table containing Records in a Database

Properties:
 - `record.channel`: A dict representing a Channel object from the Discord API. Mainly for internal use.
 - `table.database`: A Database object representing the Database this Table belongs to.
 - `table.created_at`: An ISO8601 timestamp of when the Table was created.
 - `table.records`: A list of Record objects from the Table
Methods:
 - `table.get_records(field_name="field_value", field_name_2="second_filter_value")`: Finds records from the Table with the specified filters. Returns a list of Record objects, even if only a single record is returned. May be an empty list.
 - `table.update_records("field_name_to_update", "new_value", field_name="field_value", field_name_2="second_filter_value")`: Updates the specified field name to the new value. kwargs are filters. Can update multiple records. Returns a list of updated Record objects. May be an empty list.
 - `table.create_record(field_value_1, field_value_2...)`: Creates a new Record in a Table. Returns a Record object. Expects the same amount of positional args as there are fields in a database, with each posarg corresponding to a field.

### Database
`classes.database`

Represents a Database

Properties:
 - `record.category`: A dict representing a Category object from the Discord API. Mainly for internal use.
 - `database.created_at`: An ISO8601 timestamp of when the Database was created.
 - `database.tables`: A list of Table objects, one for each Table in the database. May be an empty list.
Methods:
 - `database.create_table("name", ["list", "of", "field", "names"])`: Creates a new Table in the database.
 - `database.remove_table("name")`: Deletes a Table permanently.
 - `database.get_table("name")`: Returns the Table object from that Database with the name.
 
## Exceptions
### Global Exceptions
#### Discord404Exception
Thrown when the Discord API returns a 404.
#### Discord403Exception
Thrown when the Discord API returns a 403.
### Record Exceptions
#### DataTooLongException
Thrown when `update_field` is given too much data for a single Discord message.
### Table Exceptions
#### Not Enough Positional Arguments
Thrown when `create_record` isn't supplied with enough arguments to match the amount of fields.
#### DataTooLongException
Thrown when `create_record` is given too much data for a single Discord message.
### Database Exceptions
#### TableNotFoundException
Thrown when `get_table` cannot find a table with the specified name.
#### TooManyTablesException
Thrown when `create_table` fails because there are already 50 Tables in a Database.
#### TooLongFieldNamesException
Thrown when `create_table` fails because, combined and with commas, the list of field names are over 2000 chars long.
#### TableExistsException
Thrown when `create_table` fails because the database name already exists in the Table.