for each, font in pairs(data.raw.font) do
    data.raw.font[each].from = "fairfax-hd"
    -- if font.from == "default" then
    --     data.raw.font[each].from = "default"
    -- elseif font.from == "default-semibold" then
    --     data.raw.font[each].from = "default"
    --     data.raw.font[each].size = data.raw.font[each].size + 1
    -- elseif font.from == "default-bold" then
    --     data.raw.font[each].from = "default"
    --     data.raw.font[each].size = data.raw.font[each].size + 2
    -- elseif font.from == "locale-pick" then
    --     data.raw.font[each].from = "default"
    -- end
end
