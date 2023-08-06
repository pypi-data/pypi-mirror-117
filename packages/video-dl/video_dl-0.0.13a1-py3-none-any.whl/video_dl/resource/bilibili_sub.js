function parser_config(title) {
    return {
        font: "黑体",
        alpha: .2,
        duration: n=>{
            switch (n.type) {
            case 4:
            case 5:
                return 4;
            default:
                return 6
            }
        },
        blockTypes: [7, 8],
        resolution: {
            x: 1920,
            y: 1080
        },
        bottomMarginPercent: 0,
        bold: true,
        title: title,
        blockFilter: n=>{return true}
    }
}

function xmlDanmakus(title, jsonDanmakus) {
    function e(t, i, e) {
        if (i in t) {
            Object.defineProperty(t, i, {
                value: e,
                enumerable: true,
                configurable: true,
                writable: true
            })
        } else {
            t[i] = e
        }
        return t
    }
	
	    let r;
    (function(t) {
        t[t["Normal"] = 1] = "Normal";
        t[t["Normal2"] = 2] = "Normal2";
        t[t["Normal3"] = 3] = "Normal3";
        t[t["Bottom"] = 4] = "Bottom";
        t[t["Top"] = 5] = "Top";
        t[t["Reversed"] = 6] = "Reversed";
        t[t["Special"] = 7] = "Special";
        t[t["Special2"] = 8] = "Special2"
    }
    )(r || (r = {}));

    class o {
        constructor({content: t, time: i, type: o, fontSize: s, color: a}) {
            e(this, "content", void 0);
            e(this, "time", void 0);
            e(this, "startTime", void 0);
            e(this, "type", void 0);
            e(this, "fontSize", void 0);
            e(this, "color", void 0);
            this.content = t;
            this.time = i;
            this.startTime = parseFloat(i);
            this.type = parseInt(o);
            this.fontSize = parseFloat(s);
            this.color = parseInt(a)
        }
    }
    class s extends o {
        constructor({content: t, time: i, type: o, fontSize: s, color: a, timeStamp: r, pool: n, userHash: h, rowId: l}) {
            super({
                content: t,
                time: i,
                type: o,
                fontSize: s,
                color: a
            });
            e(this, "timeStamp", void 0);
            e(this, "pool", void 0);
            e(this, "userHash", void 0);
            e(this, "rowId", void 0);
            e(this, "pDataArray", void 0);
            this.timeStamp = parseInt(r);
            this.pool = parseInt(n);
            this.userHash = h;
            this.rowId = parseInt(l);
            this.pDataArray = [i, o, s, a, r, n, h, l]
        }
        text() {
            const t = this.pDataArray.join(",");
            return `<d p="${t}">${this.content}</d>`
        }
        static parse(t) {
            const i = t.getAttribute("p");
            const [e,o,a,r,n,h,l,c] = i.split(",");
            const u = t.innerHTML;
            return new s({
                content: u,
                time: e,
                type: o,
                fontSize: a,
                color: r,
                timeStamp: n,
                pool: h,
                userHash: l,
                rowId: c
            })
        }
    }

class n extends o {
        constructor({content: t, time: i, type: o, fontSize: s, color: a, typeTag: r, colorTag: n, endTime: h}) {
            super({
                content: t,
                time: i,
                type: o,
                fontSize: s,
                color: a
            });
            e(this, "typeTag", void 0);
            e(this, "colorTag", void 0);
            e(this, "endTime", void 0);
            this.typeTag = r;
            this.colorTag = n;
            this.endTime = h
        }
        text(t) {
            let i = t[this.fontSize];
            if (!i) {
                i = t[25]
            }
            const e = i.match(/Style:(.*?),/)[1].trim();
            return `Dialogue: 0,${this.time},${this.endTime},${e},,0,0,0,,{${this.typeTag}${this.colorTag}}${this.content}`
        }
    }

class l {
        constructor(t, i, o, s) {
            e(this, "horizontalStack", void 0);
            e(this, "horizontalTrack", void 0);
            e(this, "verticalStack", void 0);
            e(this, "verticalTrack", void 0);
            e(this, "resolution", void 0);
            e(this, "duration", void 0);
            e(this, "canvas", void 0);
            e(this, "context", void 0);
            e(this, "fontSizes", void 0);
            e(this, "bottomMarginPercent", void 0);
            e(this, "danmakuHeight", void 0);
            e(this, "trackHeight", void 0);
            e(this, "trackCount", void 0);
            this.horizontalStack = [];
            this.horizontalTrack = [];
            this.verticalStack = [];
            this.verticalTrack = [];
            this.resolution = i;
            this.duration = o;
            //this.canvas = document.createElement("canvas");
            //this.context = this.canvas.getContext("2d");
            this.fontSizes = {
                30: `64px ${t}`,
                25: `52px ${t}`,
                18: `36px ${t}`,
                45: `90px ${t}`
            };
            this.bottomMarginPercent = s;
            this.generateTracks()
        }
        generateTracks() {
			function fixed(e, t=1) {
                    const i = e.toString();
                    const o = i.indexOf(".");
                    if (o !== -1) {
                        if (i.length - o > t + 1) {
                            return i.substring(0, o + t + 1)
                        } else {
                            return i
                        }
                    } else {
                        return i + ".0"
                    }
                }
				
            const t = 52;
            this.danmakuHeight = t;
            this.trackHeight = l.margin * 2 + t;
            this.trackCount = parseInt(fixed(this.resolution.y * (1 - this.bottomMarginPercent) / this.trackHeight, 0))
        }
        getTextSize(t) {
            //this.context.font = this.fontSizes[t.fontSize];
            //const i = this.context.measureText(t.content);
            const e = t.content.length * 12;
            return [e, this.danmakuHeight / 2]
        }
        getTags(t, {targetTrack: i, initTrackNumber: e, nextTrackNumber: o, willOverlay: s, getTrackItem: a, getTag: r}) {
            const [n,h] = this.getTextSize(t);
            const c = n * 2;
            const u = this.duration(t) * c / (this.resolution.x + c) + l.nextDanmakuDelay;
            let m = e;
            let p = null;
            do {
                p = i.find((t=>s(t, m, c)));
                m += o
            } while (p && m <= this.trackCount && m >= 0);
            if (m > this.trackCount || m < 0) {
                return `\\pos(0,-999)`
            }
            m -= o;
            i.push(a(m, c, u));
            return r({
                trackNumber: m,
                x: n,
                y: h
            })
        }
        getHorizontalTags(t) {
            return this.getTags(t, {
                targetTrack: this.horizontalTrack,
                initTrackNumber: 0,
                nextTrackNumber: 1,
                willOverlay: (i,e,o)=>{
                    if (i.trackNumber !== e) {
                        return false
                    }
                    if (i.width < o) {
                        return this.duration(t) * this.resolution.x / (this.resolution.x + o) <= i.end - t.startTime
                    } else {
                        return i.visible > t.startTime
                    }
                }
                ,
                getTrackItem: (i,e,o)=>({
                    width: e,
                    start: t.startTime,
                    visible: t.startTime + o,
                    end: t.startTime + this.duration(t),
                    trackNumber: i
                }),
                getTag: ({trackNumber: i, x: e, y: o})=>`\\move(${this.resolution.x + e},${i * this.trackHeight + l.margin + o},${-e},${i * this.trackHeight + l.margin + o},0,${this.duration(t) * 1e3})`
            })
        }
        getVerticalTags(t) {
            const i = l.danmakuType[t.type] === "top";
            return this.getTags(t, {
                targetTrack: this.verticalTrack,
                initTrackNumber: i ? 0 : this.trackCount - 1,
                nextTrackNumber: i ? 1 : -1,
                willOverlay: (i,e)=>{
                    if (i.trackNumber !== e) {
                        return false
                    }
                    return i.end > t.startTime
                }
                ,
                getTrackItem: i=>({
                    start: t.startTime,
                    end: t.startTime + this.duration(t),
                    trackNumber: i
                }),
                getTag: ({trackNumber: t, y: e})=>{
                    if (i) {
                        return `\\pos(${this.resolution.x / 2},${t * this.trackHeight + l.margin + e})`
                    } else {
                        return `\\pos(${this.resolution.x / 2},${this.resolution.y - l.margin - e - (this.trackCount - 1 - t) * this.trackHeight})`
                    }
                }
            })
        }
        push(t) {
            let i = "";
            let e = [];
            switch (l.danmakuType[t.type]) {
            case "normal":
            case "reversed":
                {
                    i = this.getHorizontalTags(t);
                    e = this.horizontalStack;
                    break
                }
            case "top":
            case "bottom":
                {
                    i = this.getVerticalTags(t);
                    e = this.verticalStack;
                    break
                }
            case "special":
            default:
                {
                    return {
                        tags: `\\pos(0,-999)`
                    }
                }
            }
            const o = {
                tags: i
            };
            e.push(o);
            return o
        }
    }
    e(l, "danmakuType", {
        [r.Normal]: "normal",
        [r.Normal2]: "normal",
        [r.Normal3]: "normal",
        [r.Bottom]: "bottom",
        [r.Top]: "top",
        [r.Reversed]: "reversed",
        [r.Special]: "special",
        [r.Special2]: "special"
    });
    e(l, "margin", 4);
    e(l, "nextDanmakuDelay", .05);

    class c {
        constructor({title: t, font: i, alpha: o, duration: s, blockTypes: a, blockFilter: r, resolution: n, bottomMarginPercent: h, bold: c}) {
            e(this, "title", void 0);
            e(this, "font", void 0);
            e(this, "alpha", void 0);
            e(this, "duration", void 0);
            e(this, "blockTypes", void 0);
            e(this, "blockFilter", void 0);
            e(this, "resolution", void 0);
            e(this, "bold", void 0);
            e(this, "danmakuStack", void 0);
            this.title = t;
            this.font = i;
            this.alpha = Math.round(o * 255).toString(16).toUpperCase().padStart(2, "0");
            this.duration = s;
            this.blockTypes = a;
            this.blockFilter = r || (()=>true);
            this.resolution = n;
            this.bold = c;
			this.danmakuStack = new l(i,n,s,h)
        }
        get fontStyles() {
            return {
                36: `Style: Larger,${this.font},72,&H${this.alpha}FFFFFF,&H${this.alpha}FFFFFF,&H${this.alpha}000000,&H${this.alpha}000000,${this.bold ? "1" : "0"},0,0,0,100,100,0,0,1,1.2,0,5,0,0,0,0`,
                30: `Style: Large,${this.font},64,&H${this.alpha}FFFFFF,&H${this.alpha}FFFFFF,&H${this.alpha}000000,&H${this.alpha}000000,${this.bold ? "1" : "0"},0,0,0,100,100,0,0,1,1.2,0,5,0,0,0,0`,
                25: `Style: Medium,${this.font},52,&H${this.alpha}FFFFFF,&H${this.alpha}FFFFFF,&H${this.alpha}000000,&H${this.alpha}000000,${this.bold ? "1" : "0"},0,0,0,100,100,0,0,1,1.2,0,5,0,0,0,0`,
                18: `Style: Small,${this.font},36,&H${this.alpha}FFFFFF,&H${this.alpha}FFFFFF,&H${this.alpha}000000,&H${this.alpha}000000,${this.bold ? "1" : "0"},0,0,0,100,100,0,0,1,1.2,0,5,0,0,0,0`,
                45: `Style: ExtraLarge,${this.font},90,&H${this.alpha}FFFFFF,&H${this.alpha}FFFFFF,&H${this.alpha}000000,&H${this.alpha}000000,${this.bold ? "1" : "0"},0,0,0,100,100,0,0,1,1.2,0,5,0,0,0,0`
            }
        }
        xmlDanmakuToAssDocument(t) {
            const i = [];
            for (const e of t) {
                if (this.blockTypes.indexOf(e.type) !== -1 || this.blockTypes.indexOf("color") !== -1 && e.color !== c.white) {
                    continue
                }
                if (!this.blockFilter(e)) {
                    continue
                }
                const [t,o] = this.convertTime(e.startTime, this.duration(e));
                i.push(new n({
                    content: this.convertText(e.content),
                    time: t,
                    endTime: o,
                    type: e.type.valueOf().toString(),
                    fontSize: e.fontSize.toString(),
                    color: e.color.toString(),
                    typeTag: this.convertType(e),
                    colorTag: this.convertColor(e.color)
                }))
            }
            return new h(i,this.title,this.fontStyles,this.blockTypes,this.resolution)
        }
        xmlStringToAssDocument(t) {
            const i = new a(t);
            return this.xmlDanmakuToAssDocument(i.danmakus.sort(((t,i)=>t.startTime - i.startTime)))
        }
        convertText(t) {
            const i = {
                "{": "｛",
                "}": "｝",
                "&amp;": "&",
                "&lt;": "<",
                "&gt;": ">",
                "&quot;": '"',
                "&apos;": "'"
            };
            for (const [e,o] of Object.entries(i)) {
                t = t.replace(new RegExp(e,"g"), o)
            }
            return t
        }
        convertType(t) {
            return this.danmakuStack.push(t).tags
        }
        convertColor(t) {
            if (t === c.white) {
                return ""
            }
            const i = t.toString(16);
            const e = i.substring(0, 2);
            const o = i.substring(2, 4);
            const s = i.substring(4, 6);
            return `\\c&H${s}${o}${e}&`
        }
        convertTime(t, i) {
            function e(t) {
                const [i,e="00"] = String(t).split(".");
                return `${i.padStart(2, "0")}.${e.substr(0, 2).padEnd(2, "0")}`
            }
            function o(t) {
                let i = 0;
                let o = 0;
                while (t >= 60) {
                    t -= 60;
                    o++
                }
                while (o >= 60) {
                    o -= 60;
                    i++
                }
                return `${i}:${String(o).padStart(2, "0")}:${e(t)}`
            }
            return [o(t), o(t + i)]
        }
    }
    e(c, "white", 16777215);
	
	class h {
        constructor(t, i, o, s, a) {
            e(this, "danmakus", void 0);
            e(this, "title", void 0);
            e(this, "fontStyles", void 0);
            e(this, "blockTypes", void 0);
            e(this, "resolution", void 0);
            this.danmakus = t;
            this.title = i;
            this.fontStyles = o;
            this.blockTypes = s;
            this.resolution = a
        }
        generateAss() {
            const t = `\n[Script Info]\n; Script generated by Bilibili Evolved Danmaku Converter\n; https://github.com/the1812/Bilibili-Evolved/\nTitle: ${this.title}\nScriptType: v4.00+\nPlayResX: ${this.resolution.x}\nPlayResY: ${this.resolution.y}\nTimer: 10.0000\nWrapStyle: 2\nScaledBorderAndShadow: no\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n${Object.values(this.fontStyles).join("\n")}\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n`.trim();
            return t + "\n" + this.danmakus.map((t=>t.text(this.fontStyles))).filter((t=>t !== "")).join("\n")
        }
    }

    var step1 = jsonDanmakus.map((i=>{
        var t, e, s, o, a, n, d, r, c, h, l, u;
        return {
            content: i.content,
            time: i.progress ? (i.progress / 1e3).toString() : "0",
            type: (t = (e = i.mode) === null || e === void 0 ? void 0 : e.toString()) !== null && t !== void 0 ? t : "1",
            fontSize: (s = (o = i.fontsize) === null || o === void 0 ? void 0 : o.toString()) !== null && s !== void 0 ? s : "25",
            color: (a = (n = i.color) === null || n === void 0 ? void 0 : n.toString()) !== null && a !== void 0 ? a : "16777215",
            timeStamp: (d = (r = i.ctime) === null || r === void 0 ? void 0 : r.toString()) !== null && d !== void 0 ? d : "0",
            pool: (c = (h = i.pool) === null || h === void 0 ? void 0 : h.toString()) !== null && c !== void 0 ? c : "0",
            userHash: (l = i.midHash) !== null && l !== void 0 ? l : "0",
            rowId: (u = i.idStr) !== null && u !== void 0 ? u : "0"
        }
    }
    ));

    step1 = step1.map((n=>new s(n)));
    const danmu_parser = new c(parser_config(title));
    step1 = danmu_parser.xmlDanmakuToAssDocument(step1);
    return step1.generateAss();
}
