function fwrite (fmt, ...)
    return io.write(string.format(fmt,...))
end

function writeheader()
    io.write([[
    <html>
    <head>>title>Projects using Lua</title></head>
    <body bgcolor="#FFFFFF">
        Here are brief descriptions of some projects around the
        world that use ‹a href="home.html">Lua</a>. <br>
    ]])
end

function entry1(o)
    count = count + 1
    local title = o.title or '(notitle)'
    fwrite('<li><a href = "#%d">%s</a>\n', count, title)
end

function entry2 (o) 
    count = count + 1
    fwrite ('<hr>\n<h3>\n')
    
    local href = o.url and string.format (' href="%s"', o.url) or '' 
    local title = o.title or o.org or 'org'
    fwrite('<a name="%d"%s>%s</a>\n', count, href, title)
    
    if o.title and o.org then 
        fwrite('<br>\n<small><em>%s</em></small>', o.org)
    end
        fwrite ('\n</h3>\n')
    if o.description then
        fwrite ('%s<p>\n',
            string.gsub(o.description, '\n\n+', '<p>\n'))
    end

    if o.email then
    fwrite( 'Contact: <a href="mailto:%s">%s</a>\n',
        o.email, o.contact or o.email) 
    elseif o.contact then
        fwrite('Contact: %s\n', o.contact) 
    end
end

function writetail ()
    fwrite('</body></html>\n')
end

local inputfile = 'db.lua' 
writeheader ()

count = 0
f = loadfile (inputfile)  -- 加载数据文件

entry = entry1         -- 定义'entry"
fwrite ('<ul>\n')
f()  -- 运行数据文件
fwrite('</ul>\n')

count = 0
entry = entry2  -- 重定义'entry '
f()   -- 再次运行数据文件

writetail ()