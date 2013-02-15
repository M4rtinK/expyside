import QtQuick 1.1
import com.nokia.meego 1.0
import com.nokia.extras 1.0

PageStackWindow {
    anchors.fill : parent
    id: rootWindow
    initialPage : mainPage
    showStatusBar : false
    showToolBar : true

    /* trigger notification
       with a given message */
    function notify(text) {
        notification.text = text;
        notification.show()
        }

    /** Grey background **/

    Page {
        /** Window content **/
        id : mainPage
        anchors.fill : parent
        tools : commonTools
        Flickable {
            anchors.topMargin : 16
            anchors.fill : parent
            //anchors.centerIn : parent
            Column {
                anchors.fill : parent
                spacing : 16
                Text {
                    text: "<h1>PySide & QtC @ Android Example</h1>"
                    anchors.horizontalCenter: parent.horizontalCenter
                }
                Text {
                    text: example.getDate()
                    font.pixelSize : 32
                    anchors.horizontalCenter: parent.horizontalCenter
                }
                TextField {
                    anchors.horizontalCenter: parent.horizontalCenter
                    id : entryField
                    width : 400
                    height : 52
                    text : "image caption"
                }
                Image {
                    id : pysideImage
                    anchors.horizontalCenter: parent.horizontalCenter
                    width : 300
                    height : 157
                    smooth : true
                    // NOTE: the image provider name in the Image.source URL is automatically lower-cased !!
                    source : "image://from_python/" + entryField.text
                }
                Button {
                    anchors.horizontalCenter: parent.horizontalCenter
                    width : 350
                    id : startButton
                    text : "notification"
                    onClicked : {
                        example.notify("entry field content:<br><b>" + entryField.text + "</b>")
                    }
                }
            }
        }
    }


        ToolBarLayout {
            id: commonTools
            visible: true
            ToolButton { text: "One" }
            ToolButton { text: "Two" }
            ToolButton { text: "tools"
                onClicked : toolsMenu.open()
            }
            ToolIcon {
                platformIconId: "toolbar-view-menu"
                anchors.right: (parent === undefined) ? undefined : parent.right
                onClicked: (myMenu.status == DialogStatus.Closed) ? myMenu.open() : myMenu.close()
            }
        }
        Menu {
            id: myMenu
            visualParent: pageStack
            MenuLayout {
                MenuItem { text: qsTr("Sample menu item 1") }
                MenuItem { text: qsTr("Sample menu item 2") }
                MenuItem { text: qsTr("Sample menu item 3") }
                MenuItem { text: qsTr("Sample menu item 4") }
                MenuItem { text: qsTr("Sample menu item 5") }
            }
        }

        Menu {
            id: toolsMenu
            visualParent: pageStack
            MenuLayout {
                Label {
                    text : "Image rotation"
                }
                Slider {
                    stepSize : 1
                    minimumValue : 0
                    maximumValue : 360
                    valueIndicatorVisible : true
                    value : pysideImage.rotation
                    onValueChanged : {
                        pysideImage.rotation = value
                    }


                }
                Label {
                    text : "Image opacity"
                }
                Slider {
                    stepSize : 0.01
                    minimumValue : 0.0
                    maximumValue : 1.0
                    valueIndicatorVisible : true
                    value : pysideImage.opacity
                    onValueChanged : {
                        pysideImage.opacity = value
                    }
                }
            }
        }


    /** Notification banner **/

    InfoBanner {
        id: notification
        timerShowTime : 5000
        height : rootWindow.height/5.0
        // prevent overlapping with status bar
        y : 8

    }
}