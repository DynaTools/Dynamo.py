
# Create TaskDialog

This option involves first creating the TaskDialog using its constructor, setting its properties individually and then using the `Show()` method to display it. This approach will allow access to more settings. For this reason, in cases where you want to interact with the user, it will be the most recommendable option.

Here is an example of how to perform this task.

First, the instance of the `TaskDialog` class is constructed, defining the title, header and body of the pop-up window.

```python
dialog = TaskDialog("Title")
dialog.MainInstruction = "Header"
dialog.MainContent = "Body"
```

## Buttons

Once the base structure of the window is created, the buttons can be created through the `CommonButtons` property. You can add as many as the values defined in the enumerated `TaskDialogCommonButtons`. It simply has to be separated with the "|" symbol.

Possible Buttons:

- `TaskDialogCommonButtons.Ok`
- `TaskDialogCommonButtons.Yes`
- `TaskDialogCommonButtons.No`
- `TaskDialogCommonButtons.Cancel`
- `TaskDialogCommonButtons.Retry`
- `TaskDialogCommonButtons.Close`

The following is an example of how to create the "Yes" and "No" buttons:

```python
dialog.CommonButtons = TaskDialogCommonButtons.Yes | TaskDialogCommonButtons.No
```

It is also possible to add a selectable field of type Yes/No. The `VerificationText` property shall be used for this purpose.

```python
dialog.VerificationText = "Yes/No"
```

Alternatively, to the `VerificationText` you can create an `ExtraCheckBoxText` which has identical behavior. Only one of them can be created, but never at the same time.

```python
dialog.ExtraCheckBoxText = "Another selection"
```

## Progress Bar

The `EnableMarqueeProgressBar` property will allow a progress bar to be displayed while all the options available in the pop-up window are configured.

```python
dialog.EnableMarqueeProgressBar = True
```

A progress bar is a window that an application can use to indicate the progress of a long operation. It consists of a rectangle that shows a progress bar that animates as an operation progresses. The animation continues until the TaskDialog is closed.
